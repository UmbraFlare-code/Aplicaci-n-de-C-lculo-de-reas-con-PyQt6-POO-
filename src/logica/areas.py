import math

class Circulo:
    """Clase que representa un círculo.
    
    Esta clase permite crear y manipular círculos, calculando su área
    a partir del radio proporcionado.

    Args:
        radio (float): Radio del círculo. Debe ser un número positivo mayor que cero.

    Raises:
        ValueError: Si el radio es menor o igual a cero.

    Examples:
        >>> circulo = Circulo(5.0)
        >>> area = circulo.calcular_area()
        >>> print(f"Área: {area:.2f}")
        Área: 78.54
    """

    def __init__(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo usando la fórmula π * r².

        Returns:
            float: Área del círculo en unidades cuadradas.

        Examples:
            >>> circulo = Circulo(2.0)
            >>> area = circulo.calcular_area()
            >>> print(f"Área: {area:.2f}")
            Área: 12.57
        """
        return math.pi * self.radio ** 2


class Triangulo:
    """Clase que representa un triángulo.
    
    Esta clase permite crear y manipular triángulos, calculando su área
    a partir de la base y altura proporcionadas.

    Args:
        base (float): Base del triángulo. Debe ser un número positivo mayor que cero.
        altura (float): Altura del triángulo. Debe ser un número positivo mayor que cero.

    Raises:
        ValueError: Si la base o la altura son menores o iguales a cero.

    Examples:
        >>> triangulo = Triangulo(4.0, 3.0)
        >>> area = triangulo.calcular_area()
        >>> print(f"Área: {area:.2f}")
        Área: 6.00
    """

    def __init__(self, base: float, altura: float):
        if base <= 0:
            raise ValueError("La base debe ser un número positivo.")
        if altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del triángulo usando la fórmula (base * altura) / 2.

        Returns:
            float: Área del triángulo en unidades cuadradas.

        Examples:
            >>> triangulo = Triangulo(6.0, 4.0)
            >>> area = triangulo.calcular_area()
            >>> print(f"Área: {area:.2f}")
            Área: 12.00
        """
        return (self.base * self.altura) / 2


class Rectangulo:
    """Clase que representa un rectángulo.
    
    Esta clase permite crear y manipular rectángulos, calculando su área
    a partir de la base y altura proporcionadas.

    Args:
        base (float): Base del rectángulo. Debe ser un número positivo mayor que cero.
        altura (float): Altura del rectángulo. Debe ser un número positivo mayor que cero.

    Raises:
        ValueError: Si la base o la altura son menores o iguales a cero.

    Examples:
        >>> rectangulo = Rectangulo(5.0, 3.0)
        >>> area = rectangulo.calcular_area()
        >>> print(f"Área: {area:.2f}")
        Área: 15.00
    """

    def __init__(self, base: float, altura: float):
        if base <= 0:
            raise ValueError("La base debe ser un número positivo.")
        if altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo usando la fórmula base * altura.

        Returns:
            float: Área del rectángulo en unidades cuadradas.

        Examples:
            >>> rectangulo = Rectangulo(4.0, 2.0)
            >>> area = rectangulo.calcular_area()
            >>> print(f"Área: {area:.2f}")
            Área: 8.00
        """
        return self.base * self.altura


class Cuadrado:
    """Clase que representa un cuadrado.
    
    Esta clase permite crear y manipular cuadrados, calculando su área
    a partir del lado proporcionado.

    Args:
        lado (float): Lado del cuadrado. Debe ser un número positivo mayor que cero.

    Raises:
        ValueError: Si el lado es menor o igual a cero.

    Examples:
        >>> cuadrado = Cuadrado(4.0)
        >>> area = cuadrado.calcular_area()
        >>> print(f"Área: {area:.2f}")
        Área: 16.00
    """

    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        self.lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del cuadrado usando la fórmula lado².

        Returns:
            float: Área del cuadrado en unidades cuadradas.

        Examples:
            >>> cuadrado = Cuadrado(3.0)
            >>> area = cuadrado.calcular_area()
            >>> print(f"Área: {area:.2f}")
            Área: 9.00
        """
        return self.lado ** 2
