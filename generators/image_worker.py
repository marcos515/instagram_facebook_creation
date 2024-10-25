from PIL import Image
import hashlib
import random

def remove_metadata(image_path, output_path):
    # Abre a imagem
    with Image.open(image_path) as img:
        # Cria uma nova imagem para remover metadados
        data = list(img.getdata())
        image_without_metadata = Image.new(img.mode, img.size)
        image_without_metadata.putdata(data)

        # Salva a imagem sem metadados
        image_without_metadata.save(output_path)
        
# Carregar a imagem e modificar um pixel aleatoriamente
def modify_image_to_change_hash(image_path, output_path):
    with Image.open(image_path) as img:
        # Pegar os dados da imagem
        pixels = img.load()
        
        # Modificar um pixel aleatório para alterar o hash
        width, height = img.size
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        # Alterar levemente o valor RGB do pixel selecionado
        r, g, b = pixels[x, y]
        pixels[x, y] = (r, g, (b + 1) % 256)  # Modificando o canal azul levemente
        
        # Salvar a imagem modificada
        img.save(output_path)

# Gerar hash MD5 da imagem
def generate_image_hash(image_path):
    hasher = hashlib.md5()
    with open(image_path, 'rb') as img_file:
        buf = img_file.read()
        hasher.update(buf)
    return hasher.hexdigest()
