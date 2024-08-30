class Vacancy:
    """
    Класс для формирования вакансии
    """

    __slots__ = (
        "__name",
        "__salary_from",
        "__salary_to",
        "__description",
        "__city",
        "__link",
    )

    def __init__(self, vacancy):
        self.__name = (
            vacancy["name"] if vacancy["name"] else "Название вакансии не указано"
        )

        self.__salary_from = (
            vacancy["salary"]["from"]
            if vacancy["salary"] and vacancy["salary"]["from"]
            else 0
        )
        self.__salary_to = (
            vacancy["salary"]["to"]
            if vacancy["salary"] and vacancy["salary"]["to"]
            else 0
        )
        self.__description = (
            vacancy["snippet"]["responsibility"]
            if vacancy["snippet"] and vacancy["snippet"]["responsibility"]
            else "Описание отсутствует"
        )

        self.__city = (
            vacancy["area"]["name"]
            if vacancy["area"] and vacancy["area"]["name"]
            else "Город не указан"
        )

        self.__link = (
            vacancy["alternate_url"]
            if vacancy["alternate_url"]
            else "Ссылка не указана"
        )

    @property
    def name(self):
        return self.__name

    @property
    def link(self):
        return self.__link

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def description(self):
        return self.__description

    @property
    def city(self):
        return self.__city

    def __str__(self) -> str:
        name = f"Вакансия: {self.name}"
        salary = f"Зарплата от: {self.__salary_from} до {self.__salary_to}"
        description = f"Описание: {self.description}"
        city = f"Город: {self.city}"
        link = f"Ссылка: {self.link}"
        return f"{name}\n{salary}\n{description}\n{city}\n{link}"

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary


if __name__ == "__main__":
    vacancy1 = {
        "name": "повар",
        "alternate_url": "ссылка",
        "salary": {"from": 10000, "to": 15000},
        "snippet": {"responsibility": "требуется повар"},
        "area": {"name": "Екатеринбург"},
    }
    vacancy2 = {
        "name": "таксист",
        "alternate_url": None,
        "salary": {"from": 10000, "to": 15000},
        "snippet": None,
        "area": {"name": "Екатеринбург"},
    }
    x = Vacancy(vacancy1)
    print(x)
    y = Vacancy(vacancy2)
    print(y)
