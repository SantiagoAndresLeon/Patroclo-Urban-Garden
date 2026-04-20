import re

file_path = r'c:\Users\Santiago Leon\Desktop\Pagina web Huerta\patroclo-huerta-main\Patroclo-Urban-Garden\especies.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = '<section class="secciones catalogo-grid">'
end_tag = '</section>'

start_idx = content.find(start_tag) + len(start_tag)
end_idx = content.find(end_tag)

if start_idx == -1 or end_idx == -1:
    print('Could not find boundaries')
    exit(1)

cards_str = content[start_idx:end_idx]

cards = re.findall(r'<div class="card">.*?</div>', cards_str, re.DOTALL)

def get_title(card):
    match = re.search(r'<h3>(.*?)</h3>', card)
    if match:
        name = match.group(1).strip()
        name = name.lower()
        name = name.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        return name
    return ''

cards_sorted = sorted(cards, key=get_title)

new_cards_str = '\n\n        '.join(cards_sorted)
new_cards_str = '\n\n        ' + new_cards_str + '\n\n    '

new_content = content[:start_idx] + new_cards_str + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully sorted the cards!')
