#include <ESP8266WiFi.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>

const char *host = "192.168.1.4";

void setup() {
  Serial.begin(115200);
  Serial.println(); Serial.println("Starting CalcProbe client");

  WiFi.begin("SSID", "PASS");

  Serial.print("Connecting ");
  while (WiFi.status()!= WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.println();

  Serial.print("Connected, IP address: "); Serial.println(WiFi.localIP());
}

void loop() {
  /* Add server request for PHP */
  /* Get menu request */
  
}
