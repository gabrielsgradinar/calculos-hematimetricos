import 'package:flutter/material.dart';

class ChcmPage extends StatelessWidget {
  const ChcmPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          height: 200,
          width: MediaQuery.of(context).size.width,
          decoration: BoxDecoration(color: Colors.red),
          child: Center(
            child: Text(
              "CHCM",
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
