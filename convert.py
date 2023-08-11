import os
import subprocess

def convert_images_to_pdf(image_folder):
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]
    image_files.sort(key=lambda x: x.split('.')[0])
    
    pdf_filename = os.path.basename(image_folder) + '.pdf'
    
    # Prepare the list of image files with their full paths
    image_paths = [os.path.join(image_folder, image_file) for image_file in image_files]
    
    # Construct the magick command using the image paths
    magick_command = ['magick', 'convert'] + image_paths + [pdf_filename]
    
    # Run the magick command
    subprocess.run(magick_command)

def main():
    current_folder = os.getcwd()
    
    for subfolder in os.listdir(current_folder):
        subfolder_path = os.path.join(current_folder, subfolder)
        if os.path.isdir(subfolder_path):
            convert_images_to_pdf(subfolder_path)

if __name__ == "__main__":
    main()
