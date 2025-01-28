

class Type1:
    """
    A class used to represent a Type1 object.

    Attributes
    ----------
    name : str
        the name of the objec set_namet
    phone : int
        the phone number associated with the object

    Methods
    -------
    set_name(new_name: str)
        Sets the name of the object to new_name
        if it is different from the current name.

    set_phone(new_phone: int)
        Sets the phone number of the object to new_phone 
        if it is different from the current phone number.

    __str__()
        Returns a string representation of the object.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Type1 object.
        """
        self.name: str = "Type1"
        self.phone: int = 1234567890

    def set_name(self, new_name: str) -> None:
        """
        Sets a new name if it is different from the current name.

        Args:
            new_name (str): The new name to be set.

        Returns:
            None
        """
        if self.name != new_name:
            self.name = new_name
            print("Name changed to: ", self.name)
        else:
            print("Name is already: ", self.name)

    def set_phone(self, new_phone: int) -> None:
        """
        Sets the phone number to a new value if it is different from the current one.

        Args:
            new_phone (int): The new phone number to set.

        Returns:
            None
        """
        if self.phone != new_phone:
            self.phone = new_phone
            print("Phone changed to: ", self.phone)
        else:
            print("Phone is already: ", self.phone)

    # method to print the object
    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        The string includes the name and phone attributes of the object.

        Returns:
            str: A formatted string containing the name and phone.
        """
        return f"Name: {self.name}, Phone: {self.phone}"


# main code to test this class
# Note - install the plugins in ./vscode/extensions.json 
# Use `code --list-extensions` to verify all installed extensions

if __name__ == "__main__":
    t1 = Type1()
    t1.set_name("Type1")
    t1.set_phone(1234567890)
    print(t1)

    t1.set_name("Type2")
    t1.set_phone(9876543210)
    print(t1)
    t1.set_name(12345)  # This should be underlined in red.