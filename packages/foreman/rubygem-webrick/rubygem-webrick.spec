# template: default
%global gem_name webrick

Name: rubygem-%{gem_name}
Version: 1.8.1
Release: 1%{?dist}
Summary: HTTP server toolkit
License: Ruby and BSD-2-Clause
URL: https://github.com/ruby/webrick
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.4.0
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
WEBrick is an HTTP server toolkit that can be configured as an HTTPS server, a
proxy server, and a virtual-host server.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/webrick.gemspec

%changelog
* Sun Apr 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.8.1-1
- Update to 1.8.1

* Mon Oct 10 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.7.0-1
- Add rubygem-webrick generated by gem2rpm using the default template

