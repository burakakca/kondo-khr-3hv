/**
 * run_motion
 * Example program to run a motion from the RCB-4
 *
 * Copyright 2010 - Christopher Vo (cvo1@cs.gmu.edu)
 * George Mason University - Autonomous Robotics Laboratory
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "rcb4.h"
#include <unistd.h>

KondoInstance ki;

int main(int argc, char *argv[])
{
	// check cmd-line arguments -----------------------------------------------

	printf("ok");
	// open -------------------------------------------------------------------
	int ret = kondo_init(&ki);

	ki.debug = 1;

	// play motion ------------------------------------------------------------
	//
	// it waits for at most max_wait (50 seconds) for the motion to finish,
	// and returns immediately when either 50 seconds has passed, or
	// the motion has finished. 
	//
	// if you want this function to return immediately, 
	// just pass in 0 for max_wait.
	// 
	char * hex = "F1 F2 F3";
	ret = kondo_hareket(&ki, hex);
	printf("%uc", ret);
	return 0;
}
