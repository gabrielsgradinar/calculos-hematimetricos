import 'package:flutter/material.dart';

class HcmPage extends StatelessWidget {
  const HcmPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          height: 200,
          width: MediaQuery.of(context).size.width,
          decoration: BoxDecoration(color: Colors.yellow),
          child: Center(
            child: Text(
              "HCM",
              style: TextStyle(
                color: Colors.white,
                fontSize: 30,
              ),
            ),
          ),
        ),
      ],
    );
  }
}
