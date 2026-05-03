{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python313.withPackages (ps: with ps; [
    requests
    beautifulsoup4
    selenium
  ]);
in
pkgs.mkShell {
  packages = [
    pythonEnv
    pkgs.chromium
    pkgs.chromedriver
  ];

  shellHook = ''
    export CHROMEDRIVER_PATH="${pkgs.chromedriver}/bin/chromedriver"
    export CHROME_BIN="${pkgs.chromium}/bin/chromium"
  '';
}
