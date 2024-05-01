# Created by getinet at 4/29/2024
Feature: Cart tests

#  Scenario: 'Your cart is empty' message is shown for empty cart
#    Given Open target main page
#    When Click on Cart icon

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for coffee
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation

  Scenario: User can click the sign in icon
    Given Open Target main page
    When click on 'Sign In'
    And click on 'Sign In' from navigation menu
    Then Verify Sign In form opened

  Scenario: User can Login using valid credentials
    Given Open Target main page
    When click Sign In Icon
    And click Sign In from side navigation menu
    And Input "email" and "password" on SignIn page
    And click Sign in to log in
    Then verify user is logged in







