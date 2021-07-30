Feature: Urbankissan order placing
  As a customer,
  Can able to search for products and add to basket
  Can able to place the orders from webpage

  Background:
    Given The urbankissan home page displayed

  Scenario: Basic order placing
    When The user clicks on Shop now
    And The user selects product and add to cart
    And The user clicks checkout button
    Then The user can able to see product in checkout page
