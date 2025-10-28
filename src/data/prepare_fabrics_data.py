import os
import pandas as pd

def generate_fabric_metadata(raw_dir="data/raw/TFD Textile Dataset", output_csv="data/processed/ten_fabrics_metadata.csv"):
    records = []
    for fabric_folder in sorted(os.listdir(raw_dir)):
        folder_path = os.path.join(raw_dir, fabric_folder)
        if not os.path.isdir(folder_path):
            continue

        for file in os.listdir(folder_path):
            if file.lower().endswith(('.jpg', '.png', '.jpeg')):
                image_path = os.path.join(folder_path, file)
                # Try to read corresponding .txt file for metadata if it exists
                txt_file = os.path.splitext(file)[0] + ".txt"
                txt_path = os.path.join(folder_path, txt_file)
                label = "Unknown"
                if os.path.exists(txt_path):
                    try:
                        with open(txt_path, "r", encoding="utf-8", errors="ignore") as f:
                            text = f.read().lower()
                            if "defect" in text:
                                label = "Defective"
                            elif "normal" in text or "no defect" in text:
                                label = "Normal"
                            else:
                                label = text.strip()[:50] or "Unknown"
                    except:
                        pass

                records.append({
                    "fabric_id": fabric_folder,
                    "image_name": file,
                    "defect_label": label,
                    "file_path": image_path.replace("\\", "/")
                })

    df = pd.DataFrame(records)
    df.to_csv(output_csv, index=False)
    print(f"✅ Fabric metadata CSV generated successfully! Saved to: {output_csv}")
    print(f"Total images indexed: {len(df)}")

if __name__ == "__main__":
    generate_fabric_metadata()
