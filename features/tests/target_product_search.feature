# Created by getinet at 4/10/2024
Feature: Search tests

    Scenario: User can search for a coffee
    Given Open Target main page
    When Search for 'coffee'
    Then Verify search results are shown for coffee

  Scenario: User can search for tea
    Given Open Target main page
    When Search for 'tea'
    Then Verify search results are shown for tea

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

  Scenario: Verify that User can see product names with images
    Given Open main page
    When Search for ring doorbell camera
    Then Verify that every product has a name and image

  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open Target home page
    When click on 'Cart icon'
    Then Verify cart is empty