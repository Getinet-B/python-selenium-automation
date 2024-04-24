# Created by getinet at 4/22/2024
Feature: Search for any product


  Scenario: Verify that User can see product names with images
    Given Open main page
    When Search for ring doorbell camera
    Then Verify that every product has a name and image