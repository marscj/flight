import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';

class LogIn extends StatelessWidget {
  LogIn({
    Key key,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xffffffff),
      body: Stack(
        children: <Widget>[
          Transform.translate(
            offset: Offset(56.0, 134.0),
            child: SizedBox(
              width: 230.0,
              height: 49.0,
              child: Stack(
                children: <Widget>[
                  Pinned.fromSize(
                    bounds: Rect.fromLTWH(0.0, 0.0, 230.0, 49.0),
                    size: Size(230.0, 49.0),
                    pinLeft: true,
                    pinRight: true,
                    pinTop: true,
                    pinBottom: true,
                    child: Container(
                      decoration: BoxDecoration(
                        color: const Color(0xffffffff),
                        border: Border.all(
                            width: 1.0, color: const Color(0xff707070)),
                      ),
                    ),
                  ),
                  Pinned.fromSize(
                    bounds: Rect.fromLTWH(14.0, 15.0, 50.0, 20.0),
                    size: Size(230.0, 49.0),
                    pinLeft: true,
                    fixedWidth: true,
                    fixedHeight: true,
                    child: Text(
                      'Email',
                      style: TextStyle(
                        fontFamily: 'STSong',
                        fontSize: 20,
                        color: const Color(0xff707070),
                      ),
                      textAlign: TextAlign.left,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

