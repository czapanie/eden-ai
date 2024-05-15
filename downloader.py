import bing

counter = 0
with open("data.txt", 'r', encoding='utf-8') as data:
    for i in data:
        counter += 1
    data.close()
while counter > 0:
    with open ("data.txt", 'r', encoding='utf-8') as data:
        for specie in data:
            print(specie)
            # Download images
            bing.download_images(
                specie.strip(),
                limit = 500,
                output_dir = "dataset/{}/".format(specie.strip()),
            )
            # Delete specie just downloaded and rewrite the file
            lines = data.readlines()
            counter = 0
            
            with open ("data.txt", 'w', encoding='utf-8') as data:
                for line in lines:
                    if line.strip() != specie.strip():
                        data.write(line)
                    # Recount files
                    counter += 1
                    