{
  description = "PFOSIX LifeWheelz UIXengine MVP DevShell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShells.default = pkgs.mkShell {
          name = "pfosix-devshell";

          nativeBuildInputs = with pkgs; [
            python3
            python3Packages.gradio
            python3Packages.fastapi
            python3Packages.uvicorn
            gnumake
            cargo
            rustc
          ];

          shellHook = ''
            echo "💠 PFOSIX DevShell activated!"
          '';
        };
      });
}

