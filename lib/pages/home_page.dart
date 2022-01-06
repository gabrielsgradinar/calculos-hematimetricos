import 'package:flutter/material.dart';

import 'pageViews/one_page.dart';

class HomePage extends StatefulWidget {
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  PageController _pageController = PageController();

  int indexBottomNavigationBar = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(child: Text("Calculos Hematimétricos")),
      ),
      drawer: Drawer(
        child: ListView(
          children: [
            UserAccountsDrawerHeader(
              accountName: Text("Gabriel"),
              accountEmail: Text("gabriel@gmail.com"),
              currentAccountPicture: CircleAvatar(
                backgroundColor: Colors.lightGreen,
                child: Text('G'),
              ),
            ),
            ListTile(
              onTap: () {
                _pageController.jumpToPage(0);
                Navigator.pop(context);
                setState(() {
                  indexBottomNavigationBar = 0;
                });
              },
              title: Text("Item 1"),
              trailing: Icon(Icons.arrow_forward),
            ),
            ListTile(
              onTap: () {
                _pageController.jumpToPage(1);
                Navigator.pop(context);
                setState(() {
                  indexBottomNavigationBar = 1;
                });
              },
              title: Text("Item 2"),
              trailing: Icon(Icons.arrow_forward),
            ),
            ListTile(
              onTap: () {
                _pageController.jumpToPage(2);
                Navigator.pop(context);
                setState(() {
                  indexBottomNavigationBar = 2;
                });
              },
              title: Text("Item 3"),
              trailing: Icon(Icons.arrow_forward),
            ),
          ],
        ),
      ),
      body: PageView(
        controller: _pageController,
        children: [
          OnePage(),
          Container(color: Colors.red),
          Container(color: Colors.yellow)
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: indexBottomNavigationBar,
        onTap: (int page) {
          setState(() {
            indexBottomNavigationBar = page;
          });
          _pageController.animateToPage(
            page,
            duration: Duration(milliseconds: 300),
            curve: Curves.ease,
          );
        },
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.access_alarms),
            label: "Item 1",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.access_alarms),
            label: "Item 2",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.access_alarms),
            label: "Item 3",
          ),
        ],
      ),
    );
  }
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSwatch(primarySwatch: Colors.green),
      ),
      home: HomePage(),
    );
  }
}
