# Created by getin at 4/13/2024
Feature: Verify Test


  Scenario: Verify there are 10 benefit cells
    Given Open Target Circle page
    Then Verify the right circle page
    Then Verify benefit cells has 10 cells


  Scenario: Add any Target's product into cart
    Given Open Target main page
    Then Search for 'air fryer'
    And add 'air fryer' to cart
    And add to cart from the side menu
    When Verify purchased item is in cart
