# Created by getin at 4/7/2024
Feature: Click icon tests


  Scenario: User can click the cart icon
    Given Open Target home page
    When click on 'Cart icon'
    Then Verify cart is empty
