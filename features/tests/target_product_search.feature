# Created by getin at 4/10/2024
Feature: Search tests


  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <product>
    Then Verify search results are shown for <expected_product>
    Examples:
    |product        |expected_product    |
    |milk           |milk                |
    |chocolate      |chocolate           |
    |stanley cup    |stanley cup         |
    |air purifier   |air purifier        |
    |dumbbells      |dumbbells           |