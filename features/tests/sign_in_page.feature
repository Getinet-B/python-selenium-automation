# Created by getinet at 5/10/2024
Feature: Sign In Test, Verify Error Message

  Scenario: Verify error message is shown for incorrect login
    # Enter steps here
    Given Open Target
    When click Sign In button
    And click Sign In button on side navigation menu
    Given Open sign in page
    When Enter incorrect email "getinet@example.com" and password "Password"
    And Click login button
    Then Verify error message "We can't find your account." is shown