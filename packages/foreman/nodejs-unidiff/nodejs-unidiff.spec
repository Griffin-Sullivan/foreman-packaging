%global npm_name unidiff

Name: nodejs-unidiff
Version: 1.0.2
Release: 2%{?dist}
Summary: diff with unified diff format handling
License: MIT
Group: Development/Libraries
URL: https://github.com/mvoss9000/unidiff#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(diff) >= 2.2.2
Requires: npm(diff) < 5.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package
%nodejs_fixdep diff '>= 2.2.2 < 5.0.0'

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr hunk.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr unidiff.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc readme.md

%changelog
* Wed Jul 10 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.2-2
- Allow diff 4.x

* Fri May 17 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.2-1
- Update to 1.0.2

* Wed Oct 31 2018 Ohad Levy <ohadlevy@gmail.com> 0.0.4-1
- Add nodejs-unidiff generated by npm2rpm using the single strategy

