import 'package:calculos_hematimetricos/pages/pageViews/chcm_page.dart';
import 'package:calculos_hematimetricos/pages/pageViews/hcm_page.dart';
import 'package:flutter/material.dart';

import 'pageViews/vcm_page.dart';

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
            DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
              child: Text(
                'Bem vindo !',
                style: TextStyle(fontSize: 24, color: Colors.white),
              ),
            ),
            ExpansionTile(
              title: Text("Calculos"),
              children: [
                ListTile(
                  onTap: () {
                    _pageController.jumpToPage(0);
                    Navigator.pop(context);
                  },
                  title: Text("VCM"),
                  trailing: Icon(Icons.arrow_forward),
                ),
                ListTile(
                  onTap: () {
                    _pageController.jumpToPage(1);
                    Navigator.pop(context);
                  },
                  title: Text("HCM"),
                  trailing: Icon(Icons.arrow_forward),
                ),
                ListTile(
                  onTap: () {
                    _pageController.jumpToPage(2);
                    Navigator.pop(context);
                  },
                  title: Text("CHCM"),
                  trailing: Icon(Icons.arrow_forward),
                ),
              ],
            ),
            ExpansionTile(
              title: Text("Informações"),
              children: [
                ListTile(
                  title: Text("Objetivo"),
                  trailing: Icon(Icons.arrow_forward),
                ),
                ListTile(
                  title: Text("Quem somos"),
                  trailing: Icon(Icons.arrow_forward),
                ),
                ListTile(
                  title: Text("Referências"),
                  trailing: Icon(Icons.arrow_forward),
                ),
              ],
            ),
          ],
        ),
      ),
      body: PageView(
        controller: _pageController,
        children: [
          VcmPage(),
          HcmPage(),
          ChcmPage(),
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
