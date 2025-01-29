

class Type1:
    """
    A class used to represent a Type1 object.

    Attributes
    ----------
    name : str
        the name of the objec set_namet
    serial : int
        the serial number associated with the object

    Methods
    -------
    set_name(new_name: str)
        Sets the name of the object to new_name
        if it is different from the current name.

    set_serial(new_serial: int)
        Sets the serial number of the object to new_serial 
        if it is different from the current serial number.

    __str__()
        Returns a string representation of the object.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Type1 object.
        """
        self.name: str = "Type1"
        self.serial: int = 1234567890

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

    def set_serial(self, new_serial: int) -> None:
        """
        Sets the serial number to a new value if it is different from the current one.

        Args:
            new_serial (int): The new serial number to set.

        Returns:
            None
        """
        if self.serial != new_serial:
            self.serial = new_serial
            print("Serial changed to: ", self.serial)
        else:
            print("Serial is already: ", self.serial)

    def get_next_serial(self) -> int:
        """
        Returns the next serial number to be used.

        Returns:
            int: The next serial number.
        """
        return self.serial + 1
    
    # method to print the object
    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        The string includes the name and serial attributes of the object.

        Returns:
            str: A formatted string containing the name and serial.
        """
        return f"Name: {self.name}, Serial: {self.serial}"


# main code to test this class
# Note - install the plugins in ./vscode/extensions.json 
# Use `code --list-extensions` to verify all installed extensions


if __name__ == "__main__":
    t1 = Type1()
    t1.set_name("Type1")
    t1.set_serial(1234567890)
    print(t1)

    t1.set_name("Type2")
    t1.set_serial(9876543210)
    print(t1)
    t1.set_name(12345)  # This should be underlined in red.

    # Now we see how this can break at runtime
    t1.set_serial("000")
    next_sn = t1.get_next_serial()
    print("Next serial number: ", next_sn)

