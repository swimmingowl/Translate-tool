import openai
import re

# 替换为您的OpenAI API密钥
openai.api_key = "填入API"

input_file = "填入要翻译的文件地址和名称"
output_file = "填入翻译后要保存的文件地址和名称"

def translate_text(text, target_language="chinese"):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following text to {target_language}:\n{text}\n---\n",
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    translated_text = response.choices[0].text.strip()
    
    # 检查翻译文本是否包含一个 "---" 分隔符
    separator = "---"
    if separator in translated_text:
        translated_text = translated_text.split(separator)[0].strip()
    
    return translated_text


def translate_md_file(input_file, output_file, target_language="zh"):
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    translated_lines = []
    total_lines = len(lines)
    for index, line in enumerate(lines):
        if re.match(r'^\s*$', line):
            translated_lines.append(line)
        else:
            translated_line = translate_text(line, target_language)
            translated_lines.append(translated_line + "\n")

        # 打印当前进度
        print(f"翻译进度：{index + 1}/{total_lines}")

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.writelines(translated_lines)

translate_md_file(input_file, output_file)
