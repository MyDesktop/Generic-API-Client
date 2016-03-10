#!/usr/bin/env php
<?php

$baseurl = 'https://integrations.mydesktop.com.au/api/v1.1';

$api_key = $argv[1];
$access_token = $argv[2];

if (!$api_key || !$access_token) {
    echo "Usage: client.php <api_key> <access_token>\n";
    exit();
}

// Get contacts
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
    echo "HTTP 401: Check values for access_token and api_key\n";
    exit();
}

$result = json_decode($result);

foreach (@$result->{"contacts"} as $contact) {

    echo $contact->{"firstname"} . " " . $contact->{"lastname"} . "\n";

}

?>
