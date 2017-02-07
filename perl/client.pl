#!/usr/bin/env perl

use LWP::UserAgent;
use HTTP::Request::Common;
use JSON;

my $baseurl = 'https://integrations.mydesktop.com.au/api/v1.2';
my $host = 'integrations.mydesktop.com.au:443';

my $api_key = $ARGV[0];
my $access_token = $ARGV[1];

if (!$api_key || !$access_token) {
    print "Usage: client.pl <api_key> <access_token>\n";
    exit;
}

# Get contacts
my $url = $baseurl . '/contacts?api_key=' . $api_key;

my $ua = LWP::UserAgent->new;

$ua->ssl_opts("verify_hostname" => 0);

$ua->credentials(
    "$host",
    "Authentication Required",
    "$access_token" => ""
);

my $header = HTTP::Headers->new("Accept" => "application/json");
my $req = HTTP::Request->new("GET",$url,$header);

my $response = $ua->request($req);

my $response_code = $response->code;

if ($response_code == 403) {
    print "HTTP 403: You don't have access to this operation. Check /scopes for a list of permissions granted to you. Alternatively, check your api_key value.\n";
    exit;
} elsif ($response_code == 401) {
    print "HTTP 401: Check values for access_token and api_key\n";
    exit;
}

my $result = decode_json($response->decoded_content);

my $contacts = $result->{"contacts"};

foreach my $contact (@$contacts) {
    print $contact->{"firstname"} . " " . $contact->{"lastname"} . "\n";
}

exit;
