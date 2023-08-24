# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
# greet()

#! Function with Inputs
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")   
# greet_with_name("Thinh Le")

#! Function with more than 1 input
def greet_with(name: str, location: str) -> str:
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with("Thinh Le", "Vietnam")     
