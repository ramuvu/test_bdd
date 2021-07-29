Feature: Urbankissan order placing
  As a customer,
  Can able to search for products and add to basket
  Can able to place the orders from webpage

  Background:
    Given the urbankissan home page displayed

  Scenario: Basic order placing
    When the user click on Shop now button
    When the user selects products to add
    When the user click checkout button
    Then the user can able to see product in checkout page
