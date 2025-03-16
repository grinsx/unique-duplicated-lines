def remove_duplicate_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    filtered_lines = []
    prev_content = None
    
    for line in lines:
        # 查找制表符和井号的位置
        tab_pos = line.find('\t')
        hash_pos = line.find('#')
        
        # 如果行中同时包含制表符和井号，且制表符在井号之前
        if tab_pos != -1 and hash_pos != -1 and tab_pos < hash_pos:
            # 提取制表符和井号之间的内容
            current_content = line[tab_pos+1:hash_pos]
            
            # 如果当前内容与前一行不同，或者这是第一行
            if current_content != prev_content:
                filtered_lines.append(line)
                prev_content = current_content
            # 如果相同，则跳过这一行（不添加到结果中）
        else:
            # 如果行不符合格式要求，保留该行
            filtered_lines.append(line)
            prev_content = None  # 重置前一行内容
    
    # 将结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)

# 使用示例
input_file = r'c:\Users\Downloads\导出 - 主码 - 系统词库 - 单字.txt'  # 使用您提供的文件路径
output_file = r'c:\Users\Downloads\导出 - 主码 - 系统词库 - 单字_去重.txt'  # 输出文件路径
remove_duplicate_lines(input_file, output_file)
