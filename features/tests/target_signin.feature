# Created by getin at 4/7/2024
Feature: Click Sign In icon


  Scenario: User can click the sign in icon
    Given Open Target page
    When click on 'Sign In'
    And click on 'Sign In' from navigation menu
    Then Verify Sign In form opened