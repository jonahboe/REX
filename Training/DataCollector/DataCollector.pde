PImage img;
int count = 0;
String output[] = new String[1];
int qnt[] = new int[8];

void setup() {
  size(640, 480);
  img = loadImage(count + ".png");
  
  frameRate(10);
  output[0] = "";
  for (int i = 0; i < 8; i++)
    qnt[i] = 0;
}

void draw() {
  image(img, 0, 0);
}

void mousePressed() {
  int loc = (int)map(mouseX, 0, 640, 1, 6);
  qnt[loc]++;
  takeLoc(loc);
  delay(200);
}

void keyPressed() {
  if (key == ' ') {
    qnt[0]++;
    takeLoc(0);
    delay(200);
  }
  if (key == 'c') {
    println();
    for (int i = 0; i < 6; i++)
      println(i + ": " + qnt[i]);
    println();
  }
}

void takeLoc(int loc) {
  output[0] += loc + ", ";
  saveStrings("results.txt",output);
  println(count++);
  img = loadImage(count + ".png");
  image(img, 0, 0);
}
