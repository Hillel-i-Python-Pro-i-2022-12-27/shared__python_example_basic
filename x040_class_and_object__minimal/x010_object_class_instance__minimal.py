# Object, Class, Instance.
#
# Object is as box.
#   It can contain:
#   - "variables" (called "attributes")
#   - "functions" (called "methods") for work with this variables.
#
# Class is as "custom type". As int, str, etc. In general, class is as blueprint for creating objects.
#
# Instance for "class" is an "object", created by this "class".


class HumanClass:
    # This method used to initialize values of "instance"
    def __init__(self, name: str, age: int = 18):
        self.name = name
        self.age = age

    # This method use attributes from "instance"
    def say(self) -> str:
        return f"Hi, i am {self.name}. I'm {self.age} old."

    def change_age(self, new_age: int) -> None:
        self.age = new_age


def make_actions(human_instance: HumanClass) -> None:
    print(human_instance.say())
    print(human_instance.name)
    print(type(human_instance))

    human_instance.change_age(new_age=23)
    print(human_instance.say())


if __name__ == "__main__":
    aleks = HumanClass(name="Aleks")
    make_actions(human_instance=aleks)
