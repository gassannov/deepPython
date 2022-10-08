from faker import Factory
from faker import Faker


def main():
    fake = Faker(locale="Ru_ru")
    for i in range(5):
        doc = {
            'name': fake.name(),
            'address': fake.address(),
            'company': fake.company(),
            'country': fake.country()
        }
        print(doc)


if __name__ == "__main__":
    # fake = Faker(locale="Ru_ru")
    # print(fake.word())
    main()