# Created by getin at 4/14/2024
Feature: Verify all elements on Target Help page


  Scenario: User can verity all the elements on the page
    Given Open Target help page
    Then Verify 'Target Help' title is shown
    And Verify Search Bar is shown
    And Verify Search Icon is shown
    And Verify customer menu has 7 options
    And Verify information menu has 2 box
    When Verify 'Browse all Help pages' is shown