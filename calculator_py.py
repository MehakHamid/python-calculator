{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMa2hdfPFo0hp9+bNxCYU6B",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MehakHamid/python-calculator/blob/main/calculator_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-Fwaha6Ffa5H",
        "outputId": "b7aea6aa-1d93-4485-dd2c-303388cb4e20"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Select operation:\n",
            "1. Add\n",
            "2. Subtract\n",
            "3. Multiply\n",
            "4. Divide\n",
            "Enter choice (1/2/3/4): 4\n",
            "Enter first number: 2\n",
            "Enter second number: 5\n",
            "Result: 0.4\n"
          ]
        }
      ],
      "source": [
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "def divide(x, y):\n",
        "    if y == 0:\n",
        "        return \"Error! Division by zero.\"\n",
        "    return x / y\n",
        "\n",
        "def calculator():\n",
        "    print(\"Select operation:\")\n",
        "    print(\"1. Add\")\n",
        "    print(\"2. Subtract\")\n",
        "    print(\"3. Multiply\")\n",
        "    print(\"4. Divide\")\n",
        "\n",
        "    choice = input(\"Enter choice (1/2/3/4): \")\n",
        "\n",
        "    if choice in ('1', '2', '3', '4'):\n",
        "        num1 = float(input(\"Enter first number: \"))\n",
        "        num2 = float(input(\"Enter second number: \"))\n",
        "\n",
        "        if choice == '1':\n",
        "            print(\"Result:\", add(num1, num2))\n",
        "        elif choice == '2':\n",
        "            print(\"Result:\", subtract(num1, num2))\n",
        "        elif choice == '3':\n",
        "            print(\"Result:\", multiply(num1, num2))\n",
        "        elif choice == '4':\n",
        "            print(\"Result:\", divide(num1, num2))\n",
        "    else:\n",
        "        print(\"Invalid input\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    calculator()\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Xud79t8Nfdhg"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}