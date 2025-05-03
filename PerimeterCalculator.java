import java.util.Scanner;

public class PerimeterCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            // Display menu
            System.out.println("\n--- Perimeter Calculator ---");
            System.out.println("1. Circle");
            System.out.println("2. Rectangle");
            System.out.println("3. Triangle");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    // Circle
                    System.out.print("Enter the radius of the circle: ");
                    double radius = scanner.nextDouble();
                    double circlePerimeter = 2 * Math.PI * radius;
                    System.out.printf("Perimeter of the circle = %.2f units\n", circlePerimeter);
                    break;

                case 2:
                    // Rectangle
                    System.out.print("Enter the length of the rectangle: ");
                    double length = scanner.nextDouble();
                    System.out.print("Enter the width of the rectangle: ");
                    double width = scanner.nextDouble();
                    double rectanglePerimeter = 2 * (length + width);
                    System.out.printf("Perimeter of the rectangle = %.2f units\n", rectanglePerimeter);
                    break;

                case 3:
                    // Triangle
                    System.out.print("Enter side 1 of the triangle: ");
                    double side1 = scanner.nextDouble();
                    System.out.print("Enter side 2 of the triangle: ");
                    double side2 = scanner.nextDouble();
                    System.out.print("Enter side 3 of the triangle: ");
                    double side3 = scanner.nextDouble();
                    double trianglePerimeter = side1 + side2 + side3;
                    System.out.printf("Perimeter of the triangle = %.2f units\n", trianglePerimeter);
                    break;

                case 4:
                    System.out.println("Exiting the program. Goodbye!");
                    break;

                default:
                    System.out.println("Invalid choice. Please choose again.");
            }

        } while (choice != 4);

        scanner.close();
    }
}
