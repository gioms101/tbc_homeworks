import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from web_parsing import Parcing
from mongo import CreateMongoDB


def main():

    p = Parcing()
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(p.get_urls, i) for i in range(1, 5)]

    for future in as_completed(futures):
        future.result()

    with open("data.json", 'a') as f:
        f.write("\n]")

    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mongo = CreateMongoDB(data)
    mongo.insert_data()
    print(mongo.avg_of_ingredients())
    print(mongo.avg_of_steps())
    print(mongo.most_portion())
    print(mongo.find_author())

if __name__ == '__main__':
    main()
