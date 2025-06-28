"""Image compression and batch processing script for JPEG, PNG, and WebP images.
This script compresses images in a directory and saves them to an output directory.
"""

import os
from PIL import Image


def compress_image(input_path, output_path, quality=85, max_dimension=None):
    """
    Compress an image and save it to the output path.
    Supports JPEG, PNG, and WebP formats.
    Optionally resizes the image to a maximum dimension.
    """
    try:
        img = Image.open(input_path)


        if max_dimension:
            img.thumbnail((max_dimension, max_dimension))


        file_extension = os.path.splitext(output_path)[1].lower()


        if file_extension in ['.jpg', '.jpeg']:
            img.save(
                output_path,
                "JPEG",
                quality=quality,
                optimize=True
            )
            print(
                f"Comprimida JPEG: {input_path} -> "
                f"{output_path} (Calidad: {quality})"
            )
        elif file_extension == '.png':
            img.save(
                output_path,
                "PNG",
                optimize=True,
                compress_level=9
            )
            print(
                f"Comprimida PNG: {input_path} -> "
                f"{output_path} (Optimizado)"
            )
        elif file_extension == '.webp':
            img.save(
                output_path,
                "WebP",
                quality=quality
            )
            print(
                f"Convertida a WebP: {input_path} -> "
                f"{output_path} (Calidad: {quality})"
            )
        else:
            img.save(output_path)
            print(
                "Imagen procesada (formato no JPEG/PNG/WebP): "
                f"{input_path} -> {output_path}"
            )


        original_size = os.path.getsize(input_path) / (1024 * 1024)
        compressed_size = os.path.getsize(output_path) / (1024 * 1024)
        print(
            "Tamaño original: "
            f"{original_size:.2f} MB, "
            "Tamaño comprimido: "
            f"{compressed_size:.2f} MB"
        )
        print(
            "Reducción: "
            f"{((original_size - compressed_size) / original_size * 100):.2f}%"
        )


    except FileNotFoundError:
        print(
            f"Error: No se encontró el archivo '{input_path}'"
        )
    except OSError as e:
        print(
            f"Error al procesar '{input_path}': {e}"
        )


def process_directory(input_dir, output_dir, quality=85, max_dimension=None):
    """
    Process all supported images in the input directory and compress them
    into the output directory.
    """
    # Sanitize input/output directory paths to remove quotes and whitespace
    input_dir = input_dir.strip().strip('"').strip("'")
    output_dir = output_dir.strip().strip('"').strip("'")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(
            f"Directorio de salida '{output_dir}' creado."
        )


    supported_extensions = (
        '.jpg', '.jpeg', '.png', '.webp'
    )


    for filename in os.listdir(input_dir):
        if filename.lower().endswith(supported_extensions):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            print(
                f"\nProcesando: {filename}"
            )
            compress_image(
                input_path,
                output_path,
                quality,
                max_dimension
            )
        else:
            print(
                f"Saltando archivo no soportado: {filename}"
            )


if __name__ == "__main__":
    # --- CONFIGURACIÓN POR INPUT ---
    input_dir_prompt = (
        "Directorio de imágenes originales "
        "(default: images_originales): "
    )
    input_directory = (
        input(input_dir_prompt)
        .strip()
        .strip('"')
        .strip("'")
        or "images_originales"
    )
    output_dir_prompt = (
        "Directorio de salida "
        "(default: images_comprimidas): "
    )
    output_directory = (
        input(output_dir_prompt)
        .strip()
        .strip('"')
        .strip("'")
        or "images_comprimidas"
    )
    try:
        quality_prompt = (
            "Calidad de compresión JPEG/WebP "
            "(0-100, default: 80): "
        )
        COMPRESSION_QUALITY = int(
            input(quality_prompt)
            .strip()
            or "80"
        )
    except ValueError:
        COMPRESSION_QUALITY = 80
    max_dim_prompt = (
        "Dimensión máxima del lado más largo "
        "(ej. 1920, default: 1920, None para no redimensionar): "
    )
    max_dim_input = (
        input(max_dim_prompt)
        .strip()
    )
    if max_dim_input.isdigit():
        max_image_dimension = int(max_dim_input)
    elif max_dim_input == "":
        max_image_dimension = 1920
    else:
        max_image_dimension = None

    process_directory(
        input_directory,
        output_directory,
        COMPRESSION_QUALITY,
        max_image_dimension
    )
    print(
        "\nProceso de compresión de imágenes finalizado."
    )
