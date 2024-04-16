@playlist @spotify_api @sanity
  Feature: Playlists

    @critical
    @allure.label.owner:ET
    @allure.link:https://dev.example.com/
    @allure.issue:API-123
    Scenario: Verify all playlists are returned when get all playlists endpoint is call
      As a user I want to get all the playlists from SPOTIFY API

      When I call to playlists endpoint using "GET" method and without body
      Then I receive the response and validate using "get_all_playlists" json
      And I validate the status code is 200

    @critical
    @allure.label.owner:ET
    @allure.link:https://dev.example.com/
    @allure.issue:API-123
    @acceptance
    Scenario: Verify that a playlist can be created using create playlist endpoint
      As a user I want to create a playlist from SPOTIFY API

      When I call to playlists endpoint using "POST" method and without body
      Then I receive the response and validate using "create_playlist" json
      And I validate the status code is 200
