{
  description = "PFOSIX LifeWheelz UIXengine MVP DevShell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python312Full
            python312Packages.fastapi
            python312Packages.uvicorn
            python312Packages.pyyaml
            python312Packages.gradio
          ];
          shellHook = ''
            echo "💠 PFOSIX DevShell activated!"
          '';
        };
      });
}

