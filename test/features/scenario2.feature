Feature: Placing multiple orders from Urbankissan
  As a customer,
  Should able to search for products and add to basket
  Should able to place the orders from webpage

  Background:
    Given The urbankissan home page displayed

  Scenario: Basic order placing
    When The user click on Shop now
    And  The user selects multiple products and add to basket
    And  The user clicks checkout button
    Then The user can able to see products list in checkout page
