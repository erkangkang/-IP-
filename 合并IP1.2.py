import os
import re
from datetime import datetime

def extract_ips_from_file(file_path):
    ips = set()
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    with open(file_path, 'r') as file:
        content = file.read()
        ip_matches = re.findall(ip_pattern, content)
        ips.update(ip_matches)
    
    return ips

def main():
    folder_path = '.'  # 当前文件夹路径
    
    ip_set = set()
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            ips = extract_ips_from_file(file_path)
            ip_set.update(ips)
    
    num_unique_ips = len(ip_set)
    output_file = get_output_file_name(folder_path, num_unique_ips)
    
    with open(output_file, 'w') as output:
        for ip in ip_set:
            output.write(ip + '\n')
    
    print(f"合并了 {num_unique_ips} 个去重后的IP地址，已保存到 {output_file}")

def get_output_file_name(folder_path, num_unique_ips):
    today = datetime.today().strftime('%Y%m%d')
    output_file = f"{today}_{num_unique_ips}_unique_ips.txt"
    return output_file

if __name__ == '__main__':
    main()
