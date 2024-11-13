class BenettonDataSet:
    def __init__(self):
        # Conjunto de datos hardcoded
        self.advertising = [1,2,3,4,5,6,7,8,9]
        self.sales = [2,4,6,8,10,12,14,16,18]
    
    def get_sales(self):
        return self.sales

    def get_advertising(self):
        return self.advertising


class SimpleLinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.beta_0 = 0
        self.beta_1 = 0
        self.calculate_betas()
    
    def calculate_betas(self):
        # Número de observaciones
        n = len(self.x)
        
        # Sumas necesarias
        sum_x = sum(self.x)
        sum_y = sum(self.y)
        sum_xy = sum(x * y for x, y in zip(self.x, self.y))
        sum_x_squared = sum(x ** 2 for x in self.x)
        
        # Cálculo de beta_1 y beta_0
        self.beta_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
        self.beta_0 = (sum_y - self.beta_1 * sum_x) / n
    
    def predict(self, advertising_value):
        # Predicción usando la ecuación de regresión
        return self.beta_0 + self.beta_1 * advertising_value
    
    def get_regression_equation(self):
        # Devuelve la ecuación de regresión como string
        return f"Sales = {self.beta_0:.2f} + {self.beta_1:.2f} * Advertising"


class Main:
    @staticmethod
    def run():
        # Cargar el conjunto de datos
        dataset = BenettonDataSet()
        sales = dataset.get_sales()
        advertising = dataset.get_advertising()
        
        # Crear el modelo de regresión lineal simple
        model = SimpleLinearRegression(advertising, sales)
        
        # Imprimir la ecuación de regresión
        print("Ecuación de Regresión:")
        print(model.get_regression_equation())
        
        # Bucle para preguntar si se desea hacer otra predicción
        while True:
            try:
                # Solicitar un valor de advertising para predecir ventas
                advertising_value = float(input("Ingrese un valor de Advertising para predecir las Sales: "))
                predicted_sales = model.predict(advertising_value)
                print(f"Predicción de Sales: {predicted_sales:.2f}")
            except ValueError:
                print("Por favor, ingrese un valor numérico.")
                continue
            
            # Preguntar si el usuario quiere hacer otra predicción
            otra_prediccion = input("¿Desea calcular otro valor de Advertising? (s/n): ").strip().lower()
            if otra_prediccion != 's':
                print("Programa finalizado.")
                break

# Ejecutar la clase principal
if __name__ == "__main__":
    Main.run()