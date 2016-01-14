#!/usr/bin/env php
<?php

$baseurl = 'https://integrations.mydesktop.com.au/api/v1.0';

$api_key = $argv[1];
$refresh_token = $argv[2];

if (!$api_key || !$refresh_token) {
    echo "Usage: client.php <api_key> <refresh_token>\n";
    exit();
}

// Get an Access Token
$ch = curl_init($baseurl . '/token?api_key=' . $api_key);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_USERPWD, $refresh_token . ":" . "");  

$result = curl_exec($ch);

$response_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if ($response_code == 403) {
    echo "HTTP 403: You don't have access to this operation. Check /scopes for a list of permissions granted to you. Alternatively, check your api_key value.\n";
    exit();
} elseif ($response_code == 401) {
    echo "HTTP 401: Check values for access_token/refresh_token and api_key\n";
    exit();
}

$result = json_decode($result);

$access_token = $result->{"token"};

// We now have a token, allowing us to get contacts

// Get an Access Token
$ch = curl_init($baseurl . '/contacts?api_key=' . $api_key);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_USERPWD, $access_token . ":" . "");

$result = curl_exec($ch);

$response_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if ($response_code == 403) {
    echo "HTTP 403: You don't have access to this operation. Check /scopes for a list of permissions granted to you. Alternatively, check your api_key value.\n";
    exit();
} elseif ($response_code == 401) {
    echo "HTTP 401: Check values for access_token/refresh_token and api_key\n";
    exit();
}

$result = json_decode($result);

foreach (@$result->{"contacts"} as $contact) {

    echo $contact->{"firstname"} . " " . $contact->{"lastname"} . "\n";

}

?>
