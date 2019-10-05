
#define DC_PIN A0
#define PWM_PIN 12
#define INT_PIN 2
#define PART1
#define PART2
// #define PART3

int pulse_count;
void count_interrupt(){
	pulse_count++;
}

void setup(){
	Serial.begin(9600);
	pinMode(DC_PIN, INPUT);
	pinMode(PWM_PIN, OUTPUT);
	attachInterrupt(digitalPinToInterrupt(INT_PIN), count_interrupt, RISING);
}


void loop(){

	#ifdef PART1
		int dc_value = analogRead(DC_PIN); // Return value from 0 to 1023
		dc_value = map(dc_value, 0, 1023, 0, 255);
		analogWrite(PWM_PIN, dc_value);
		// Serial.println(dc_value);
		// analogWrite(PWM_PIN, 120);
	#endif

	#ifdef PART2
//		static last_pulse = 0;
//		static velocity = 0;
		Serial.println(pulse_count);
	#endif

	#ifdef PART3
		if (Serial.available() > 0 /*&& Serial.read() == '9'*/) {
			char incomingByte = Serial.read(); // read the incoming byte:
			if (incomingByte == '9'){
				Serial.println(pulse_count++);
			}


			// Serial.println(incomingByte);
		}
	#endif
}
