import 'package:flutter/material.dart';

class VcmPage extends StatelessWidget {
  const VcmPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          height: 200,
          width: MediaQuery.of(context).size.width,
          decoration: BoxDecoration(color: Colors.blue),
          child: Center(
            child: Text(
              "VCM",
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
