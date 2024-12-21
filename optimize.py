import json

def simplify_administrative_tree(input_file, output_file):
    # Đọc file JSON gốc
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    simplified_tree = {}
    
    # Duyệt qua các tỉnh/thành phố
    for province_code, province_data in data.items():
        province_name = province_data["name"]
        province_info = {
            "name": province_name,
            "districts": {}
        }
        
        # Duyệt qua các quận/huyện
        for district_code, district_data in province_data.get("quan-huyen", {}).items():
            district_name = district_data["name"]
            district_info = {
                "name": district_name,
                "wards": {}
            }
            
            # Duyệt qua các phường/xã
            for ward_code, ward_data in district_data.get("xa-phuong", {}).items():
                ward_name = ward_data["name"]
                district_info["wards"][ward_name] = {
                    "name": ward_name
                }
            
            province_info["districts"][district_name] = district_info
        
        simplified_tree[province_name] = province_info

    # Ghi ra file JSON mới
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(simplified_tree, f, ensure_ascii=False, indent=2)

    return simplified_tree

# Sử dụng hàm
input_file = 'tree.json'  # File JSON gốc
output_file = 'simplified_tree.json'  # File JSON đã được rút gọn
simplified_data = simplify_administrative_tree(input_file, output_file)