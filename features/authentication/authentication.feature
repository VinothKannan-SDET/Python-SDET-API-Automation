Feature: API Authentication

  @smoke @regression @bdd
  Scenario: Generate authentication token with valid credentials
    Given I have valid authentication credentials
    When I request an authentication token
    Then the authentication request should be successful
    And an authentication token should be returned

  @negative @regression @bdd
  Scenario: Reject invalid authentication credentials
    Given I have invalid authentication credentials
    When I request an authentication token
    Then the authentication request should be unsuccessful
    And the authentication reason should be "Bad credentials"
